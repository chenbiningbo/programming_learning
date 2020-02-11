goods_dict = {'4587': [4, 'aisle 2'],
              '8751': [4, 'aisle 1'],
              '1637': [4, 'aisle 3'],
              '7645': [4, 'aisle 1'],
              '5449': [4, 'aisle 3'],
              '1335': [4, 'aisle 3'],
              '3824': [4, 'aisle 1']
              }

del goods_dict['5449']
for key in goods_dict:
    print(key + '  ' + str(goods_dict[key]))
