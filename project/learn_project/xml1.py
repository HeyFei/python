import xml.etree.ElementTree as xml
data = '''
<books>
  <book>
   <title>Great American Novel</title>
   <characters>
    <character x="2">
     <name>Cliff</name>
     <desc>really great guy</desc>
    </character>
    <character x="3">
     <name>Lovely Woman</name>
     <desc>matchless beauty</desc>
    </character>
    <character x="4">
     <name>Loyal Dog</name>
     <desc>sleepy</desc>
    </character>
   </characters>
   <plot>
    Cliff meets Lovely Woman.  Loyal Dog sleeps, but wakes up to bark
    at mailman.
   </plot>
   <success type="bestseller">4</success>
   <success type="bookclubs">9</success>
   </book>
  </books>
'''

stuff = xml.fromstring(data)
lst = stuff.findall('book/characters/character')
print('Book count:', len(lst))

for item in lst:
    print('Name:', item.find('name').text)
    print('Desc:', item.find('desc').text)
    print('Attribute', item.get('x'))
    print("\n")
#print('Nmae:', tree.find('name').text)
