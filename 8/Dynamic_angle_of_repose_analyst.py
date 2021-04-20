# Created: 12/06/2019
# Author: Stefan Pantaleev
# Script for post-processing DEM simulaitons of an angle of repose test

#Importing libraries
from edempy import Deck
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import os
import os.path
import csv

#Reading in simulation data
for root, dirs, files in os.walk(os.curdir):
    for file in files:
        if file.endswith(".dem"):
            
            name=file.replace(".dem","")
            
            print ("-------------------------------------------------------")
            print ("Loading: "+str(name)+".dem")
            print ("-------------------------------------------------------")
            
            deck=Deck(os.path.join(root,file))
            
            #Reading in preferences
    
            if os.path.exists(os.path.join(root,'Dynamic_angle_of_repose_analyst_settings.txt')): 
                with open(os.path.join(root,'Dynamic_angle_of_repose_analyst_settings.txt'), 'r') as file:
                    preferences=file.readlines()
                    sim_end=float(preferences[3])
                    domain=np.array(preferences[5].split(','))
                    domain=domain.astype('float64')
                    bin_size=np.array(preferences[7].split(','))
                    bin_size=bin_size.astype('float64')
                    interval=np.array(preferences[9].split(','))
                    interval=interval.astype('float64')
                    report=str(preferences[11])
                    summary=str(preferences[13])
                    plots=str(preferences[15])
                    file.close()
                    settings=True
            else:
                settings=False
                sim_end=0
            
            #Check if simulaiton is run to the end
            if (sim_end-np.amax(deck.timestepValues)<0.001 and settings==True):
                
                print ("-------------------------------------------------------")
                print ("Processing: "+str(name)+".dem")
                print ("-------------------------------------------------------")
                
                #Finding key timesteps
                
                def find_nearest(array, value):
                    array=np.array(array)
                    timestep = (np.abs(array-value)).argmin()
                    return timestep
                
                start=find_nearest(deck.timestepValues,(interval[0]))
                end=find_nearest(deck.timestepValues,(interval[1]))
                
                #Dividing domain into bins
                
                grid_x=np.linspace(domain[0],domain[1],(domain[1]-domain[0])/bin_size[0])
                grid_y=np.linspace(domain[2],domain[3],(domain[3]-domain[2])/bin_size[1])
                
                time = np.arange(start,end+1,interval[2])
                time=time.astype(int)
                delta_mean=np.zeros(len(time))
                delta_std=np.zeros(len(time))
                delta_cov=np.zeros(len(time))
                
                plots="Yes\n"
                #Set up figure
                if (plots=="Yes\n"):
                    fig = plt.figure()
                    ax = fig.add_subplot(111, projection='3d')
                    ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
                    ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
                    ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
                
                
                for m in range(len(time)):
                    
                    #Declarinf arrays
                    delta=np.zeros(len(grid_y))
                    index_nonzero=np.zeros(len(grid_x))
                    SurfaceZ=np.zeros(shape=(len(grid_y),len(grid_x)))
                    SurfaceY=np.zeros(shape=(len(grid_y),len(grid_x)))
                    SurfaceX=np.zeros(shape=(len(grid_y),len(grid_x)))
                    Coord=np.zeros((1,3))
                
                 #Getting particle centres
                    for n in range(len(deck.creatorData.h5PTypes)):
                        Coord=np.append(Coord,deck.timestep[time[m]].particle[n].getPositions(),axis=0)
                    
                    #Loop through bins and find highest particle
                    for i in range(len(grid_y)):
                        #Find surface particles
                        for j in range (len(grid_x)):
                            index_coord=np.where((Coord[:,0]>(grid_x[j]-bin_size[0]/2)) & (Coord[:,0]<(grid_x[j]+bin_size[0]/2)) & (Coord[:,1]>(grid_y[i]-bin_size[1]/2)) & (Coord[:,1]<(grid_y[i]+bin_size[1]/2)))
                            surf=Coord[index_coord]
                            #Index zero values and get surface particles
                            if surf.shape[0]>0:
                                Max=np.argmax(surf[:,2])
                                SurfaceX[i][j]=surf[Max,0]
                                SurfaceY[i][j]=surf[Max,1]
                                SurfaceZ[i][j]=surf[Max,2]
                                index_nonzero[j]=j
                            else:
                                index_nonzero[j]=-1;
                        #Linear fit to surface particles
                        fit=np.polyfit(grid_x[index_nonzero!=-1],SurfaceZ[i][index_nonzero!=-1],1)
                        #Calculating angle of repose and statistics
                        delta[i]=math.atan(abs(fit[0]))*180/math.pi    

                        #Plot linear fits for final step
                        if (plots=="Yes\n" and m==(len(time)-1)):
                            ax.scatter(Coord[:,0],Coord[:,1],Coord[:,2],s=0.001,c="y")
                            ax.scatter(SurfaceX[i][:],SurfaceY[i][:],SurfaceZ[i][:],s=10,marker='o')
                            ax.plot(grid_x,np.ones(len(grid_x))*grid_y[i],(grid_x*fit[0]+fit[1]))
                            ax.set_xlabel('X coordinate')
                            ax.set_ylabel('Y coordinate')
                            ax.set_zlabel('Z coordinate')
                    #Calculate averages for timestep
                    delta_mean[m]=np.average(delta)
                    delta_std[m]=np.std(delta)
                    delta_cov[m]=delta_std[m]/delta_mean[m]*100
                #Calculate time-averaged values
                
                delta_t_av=np.average(delta_mean)
                delta_t_av_std=np.std(delta_mean)
                delta_t_av_cov=delta_t_av_std/delta_t_av*100
                
                #Export figure    
                if (plots=="Yes\n"):
                    plt.title(str(name))
                    plt.show(block=False)
                    fig.savefig(str(name)+'_DAoR.png',dpi=150)
                    plt.close('all')
                #Reading material parameters and interactions
                        
                Material_Parameters=deck.creatorData.materials.getMaterials()
                Interaction_Parameters=deck.creatorData.interactions.getInteractions()

                #Writing data to files
                    
                Names = ["Angle of repose (deg)","StDev (deg)","CoV (%)"]    
                Values= [delta_t_av,delta_t_av_std,delta_t_av_cov]
                Units = ["deg","deg","%"]
                Empty_Column=["","",""]
                sim_time=np.array(deck.timestepValues)
                if (report=="Yes\n"):    
                    with open(str(name) + "_Report" + ".csv", 'w', newline='') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerow(["Analysis parameters"])
                        writer.writerow(["Domain limits (m)"])
                        writer.writerow(["xmin","xmax","ymin","ymax"])
                        writer.writerow(domain)
                        writer.writerow(["Bin size (m)"])
                        writer.writerow(["bin size in x","bin size in y"])
                        writer.writerow(bin_size)
                        writer.writerow(["Temporal averaging"])
                        writer.writerow(["Start time (s)","End time (s)", "Timestep ratio"])
                        writer.writerow(interval)
                        writer.writerow(["Material parameters"])
                        writer.writerow(["Material","Poisson ratio","Shear modulus (Pa)","Density (kg/m^3)","Work function","Type"])
                        writer.writerows(Material_Parameters)
                        writer.writerow(["Interaction parameters"])
                        writer.writerow(["Interaction","Restitution","Static friction","Rolling friction"])
                        for line in Interaction_Parameters:
                            writer.writerow(line)
                        writer.writerow(["Results"])
                        for line in np.column_stack([Names,Values,Units,Empty_Column]):
                            writer.writerow(line)
                        writer.writerow(["Time (s)","Angle of repose (deg)","StDev (deg)", "CoV (%)"])
                        for line in np.transpose([sim_time[time], delta_mean,delta_std,delta_cov]):
                            writer.writerow(line)
                    csvFile.close()
                
                if (summary=="Yes\n"):
                    if os.path.exists("Summary.csv"):
                        with open("Summary.csv", 'a', newline='') as csvFile:
                            writer = csv.writer(csvFile)
                            writer.writerow(np.concatenate((str(name),Values),axis=None))
                            csvFile.close()
                    else:
                        with open("Summary.csv", 'w', newline='') as csvFile:
                            writer = csv.writer(csvFile)
                            writer.writerow(["Simulation", "Angle of repose (deg)","StDev (deg)","CoV (%)"])
                            writer.writerow(np.concatenate((str(name),Values),axis=None))
                            csvFile.close()
    
            else:
                if (settings == False):
                    print ("----------------------------------------------------------------------")
                    print (str(name)+".dem"+" : Settings file not found. Moving to next simulation")
                    print ("----------------------------------------------------------------------")
                else:
                    print ("--------------------------------------------------------------------")
                    print (str(name)+".dem"+" : Simulation unfinished. Moving to next simulation")
                    print ("--------------------------------------------------------------------")
        
print ("-------------------------------------------------------")
print ("No more simulations in the folder-analysis is complete!")        
print ("-------------------------------------------------------")            
            
            
            