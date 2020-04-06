def solution(s):

    answer = ''

    for x in s:

        if x.isupper():
            answer += ' '

        answer += x

    print( answer )
    return answer

solution("helloWorld") # "hello World"
solution("camelCase") # "camel Case"
solution("breakCamelCase") # "break Camel Case"