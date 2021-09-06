Module Module1

    Sub Main()
        'Do until loop
        Dim num1 = 0
        Do Until num1 = 10
            Console.WriteLine(num1)
            num1 += 1
        Loop

        'Do while loop
        Console.WriteLine("Do until loop")
        Dim num2 As Integer = 0
        Do While num2 <= 15
            If num2 = 8 Then Exit Do 'to exit the loop like the case of for loop
            Console.WriteLine(num2)
            num2 += 1
        Loop

        Console.ReadLine()
    End Sub

End Module
