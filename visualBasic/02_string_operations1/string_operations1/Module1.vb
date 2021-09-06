Module Module1

    Sub Main()
        Dim userString As String = Nothing
        Dim programString As String = "Catfish"
        Console.WriteLine("Type anything you want")
        userString = Console.ReadLine()
        Console.WriteLine(userString)
        userString = userString + programString + "Fishing" 'performing concatination

        'getting the length of a string
        'userName.Length eg username.Length = 10, userName.Length.Equals(10)

        'getting a substring of a string
        'userString.Substring(start, strings_to_capture)

        'converting a number to a sting
        'userString.Length.ToString()

        'formating strings
        'String.Fromat(condition eg "{0:n2}" , nameofStringToOperateOn)


        'changing cases
        'myString.Lower or myString.Upper

        'replacing a string
        'myString.Replace('a', 'n') replaces a with n

        'comparing strings
        'String.Compare(compString, useString, ignore_case=True) the answer is either o or 1









        Console.ReadLine()
    End Sub

End Module
