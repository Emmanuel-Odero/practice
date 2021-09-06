Module Module1

    Sub Main()
        Dim myInt As Integer = Nothing
        Console.WriteLine("Please Enter an Integer")
        myInt = Console.ReadLine()

        Select Case myInt
            Case 0
                Console.WriteLine("Hello")
            Case 1
                Console.WriteLine("Bye")
            Case 2
                Console.WriteLine("Goodmorning")
            Case Else
                Console.WriteLine("Your input is invalid please use 1 upto 3")

        End Select
        Console.ReadLine()

    End Sub

End Module
