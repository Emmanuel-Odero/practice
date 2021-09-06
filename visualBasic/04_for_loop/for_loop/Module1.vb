Module Module1

    Sub Main()
        Dim int1 As Integer
        For int1 = 1 To 20 'its not important to declare int1 before in for loops
            Console.WriteLine("int1 is equal to: " & int1)
        Next


        'Below is how we can use step to display specific values
        Console.WriteLine()
        For num1 = 1 To 2 Step 5
            Console.WriteLine("Current value is: " & num1)
        Next


        'exiting for loops
        Console.WriteLine()
        Console.WriteLine("Exiting the loop when we reach 23")
        For num1 = 1 To 30
            Console.WriteLine(num1)
            If num1 = 23 Then
                Exit For 'how to exit for loop
            End If
        Next

        'continuing in for loop
        Console.WriteLine()
        Console.WriteLine("Using Continue statement skip 5")
        For num1 = 1 To 30
            If num1 = 5 Or num1 = 5 Or num1 = 8 Then
                Continue For
            End If
            Console.WriteLine(num1)
        Next
        Console.ReadLine()
    End Sub
End Module
