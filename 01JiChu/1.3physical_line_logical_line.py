#所谓逻辑行（ LogicalLine） 是 Python 所看到 的单个语句。
#如果你希望在一行物理行中指定多行逻辑行， 那么你必须通过使用分号( ; )来明确表明逻辑行或语句的结束。
i = 5; print(i);

#每一行物理行最多只写入一行逻辑行
#如果你有一行非常长的代码， 你可以通过使用反斜杠将其拆分成多个物理行。 这被称作显式行连接（ Explicit Line Joining）
s = 'This is a string. \
This continues the string.'
print(s)