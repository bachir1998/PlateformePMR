from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def checker(docs):
    for d in docs:
        if (docs[d] == '' or docs[d] == None):
            return False
    
    return True

