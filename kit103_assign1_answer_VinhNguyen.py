'''
KIT103/KMA155 Programming Assignment 1: Sets
Submission script

Name: Vinh Nguyen
ID:470821 

Enter your answers to each question below, replacing None with the
code requested. Question 1 part a should be stored in ans['Q1 a']
and so on. You can use the show_answers() function from inside the
IPython console to show the result of your answers when you run
this script to evaluate all your answers.
A suggestion: Run the script first, then work out the answers in
the IPython interactive console before pasting them back here.
'''

ans = {} #an empty dictionary of answers
def show_answers(show_all=True):
    '''Prints the calculated answers to all questions.
    This function is included because it may be useful to you in
    checking your answers, but you are not required to use it.
    '''
    for a in sorted(ans):
        if show_all or ans[a] is not None:
            print('{0}: {1}'.format(a, str(ans[a]) if ans[a] is not None else 'unanswered'))


# Question 1: Set literals

ans['Q1 a'] = {1,3,5,7,9,11}
ans['Q1 b'] = {'Bruce',' Wayne', 'Selina', 'Kyle'}
ans['Q1 c'] = {'a', 'e', 'i', 'o', 'u'}

# Question 2: Set comprehensions

ans['Q2 a'] = {x**2 for x in range(1,6)}
ans['Q2 b'] = {7*x for x in range(1,6)}
ans['Q2 c'] = {x for x in ('mississippi')}

# Question 3: Relationships

# Given these definitions provide code to answer the questions from the assignment sheet.
animals = {'camel', 'cow', 'crayfish', 'chameleon', 'giraffe', 'horse', 'salmon', 'worm'}
mammals = {'camel', 'cow', 'giraffe', 'horse'}
aquatic = {'crayfish', 'salmon'}
farmed = {'cow', 'horse', 'salmon', 'worm'}
caught = {'ball', 'camel', 'horse', 'crayfish', 'salmon'}

ans['Q3 a'] = mammals < animals
ans['Q3 b'] = farmed in mammals
ans['Q3 c'] = caught <= aquatic

# Question 4: Set membership

ans['Q4 a'] = mammals - farmed
ans['Q4 b'] = animals & farmed
ans['Q4 c'] = (farmed & caught) - mammals 

# Question 5: Combinations

# Given these definitions, generate the combinations requested in the assignment sheet.
intensities = { 'sedate', 'extreme' }
activities = { 'BASE jumping', 'ironing', 'lecture viewing', 'skiing' }
clothing = { 'in pyjamas', 'in a wetsuit', 'in a tuxedo' }

ans['Q5 a'] = {(i1, i2) for i1 in intensities for i2 in activities}
ans['Q5 b'] = {(i1, i2) for i1 in activities for i2 in activities}
ans['Q5 c'] = {(i1, i2, i3) for i1 in intensities for i2 in activities for i3 in clothing}

# Question 6: Bags & Bitsets
# When checking these, note that parts (b)-(e) will look like normal decimal numbers,
# even though you will have entered binary literals in your answers to (b)-(d).
# A binary literal is just another way of expressing an integer value.

ans['Q6 a'] = {'cat':2, 'dog':1, 'mouse':3} 
ans['Q6 b'] = 0b00011
ans['Q6 c'] = 0b01101
ans['Q6 d'] = 0b00011 | 0b01101
ans['Q6 e'] = ans['Q6 b'] ^ ans['Q6 c']

#End of answers
