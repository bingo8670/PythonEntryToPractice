from collections import OrderedDict

favoriate_languages = OrderedDict()
favoriate_languages['jen'] = 'python'
favoriate_languages['sarah'] = 'c'
favoriate_languages['edward'] = 'ruby'
favoriate_languages['phil'] =  'python'

for name, language in favoriate_languages.items():
        print(name.title() + "'s favorite language is:" + language.title() + ".")
