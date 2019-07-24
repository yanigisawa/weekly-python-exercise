
def create_password_checker(min_upper, min_lower, min_punc, min_digits):
    def foo(pw):
        upper_case = len([ord(c) for c in pw if ord(c) in range(65, 91)]) - min_upper
        lower_case = len([ord(c) for c in pw if ord(c) in range(97, 123)]) - min_lower
        punc_marks = '!@#$%^&*()"'
        punc = len([c for c in pw if c in punc_marks]) - min_punc
        digits = len([ord(c) for c in pw if ord(c) in range(48, 58)]) - min_digits

        return (
            upper_case >= 0 and lower_case >= 0
            and punc >= 0 and digits >= 0
            , {
            'uppercase': upper_case,
            'lowercase': lower_case,
            'punctuation': punc,
            'digits': digits})
    return foo