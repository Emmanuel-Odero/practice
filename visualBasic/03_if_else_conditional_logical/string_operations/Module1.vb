Module Module1

    Sub Main()
        Console.WriteLine("What is your name")
        Dim userName As String = Console.ReadLine()
        Console.WriteLine() 'Creates a line in the command line.


        If userName = "Michael" Then
            Console.WriteLine("Welcome " & userName)
        ElseIf userName = "Ochara" Then
            Console.WriteLine("Welcome " & userName)

        Else
            Console.WriteLine("Sorry you are not a valid user, Check with the Admin")
        End If
        Console.ReadLine()

        'Conditional Operators
        'not equal <>
        'age >= 65 if age is greate or equal to

        'Logical Operators
        'Or eg If (userName="sam" Or userName="Tim") Then
        'And


    End Sub

End Module
