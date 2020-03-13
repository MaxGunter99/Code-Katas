
# Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# Every smiling face must have a smiling mouth that should be marked with either ) or D.

def count_smileys(arr):
    
    count = 0

    for i in arr:

        # Eyes
        if ':' in i or ';' in i:

            if 'D' in i or ')' in i:

                if len( i ) == 3:
                    if '-' in i or '~' in i:
                        count += 1

                else:
                    count += 1

    print( count )
    return count

# count_smileys([]) # 0
# count_smileys([':D',':~)',';~D',':)']) # 4
# count_smileys([':)',':(',':D',':O',':;']) # 2
# count_smileys([';]', ':[', ';*', ':$', ';-D']) # 1
# count_smileys([':(', ':oD', ':o(', ':D', ';(', ':(', ':D']) # 3