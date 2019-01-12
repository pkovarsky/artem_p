"""String Manipulation"""

fruit = 'Apple ' + 'Banana '
fruit += 'Orange'

animals = ', '.join(['Dogs', 'Cats', 'Monkeys'])
# Dogs, Cats, Monkeys

date = '%s %d %d Elvis Has Left the Planet' % ('August', 16.5, 1977)
# August 16 1977 Elvis Has Left the Planet9

fact = '%(first)s %(last)s is not dead, he just went home!' % {
    'first': 'Elvis', 'last': 'Presley'}
print(fact)
# Elvis Presley is not dead, he just went home!
