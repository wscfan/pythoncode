import random

def randNum():
    return str(random.randint(0, 9))

def main():
    filename = 'aa.txt'
    file = open(filename, 'w', encoding='utf-8')
    str = '赵,钱,孙,李,周,吴,郑,王,冯,陈,褚,卫,蒋,沈,韩,杨,朱,秦,尤,许,何,吕,施,张,孔,曹,严,华,金,魏,陶,姜,戚,谢,邹,喻,柏,水,窦,章,云,苏,潘,葛,奚,范,彭,郎,鲁,韦,昌,马,苗,凤,花,方,俞,任,袁,柳,酆,鲍,史,唐,费,廉,岑,薛,雷,贺,倪,汤,滕,殷,罗,毕,郝,邬,安,常,乐,于,时,傅,皮,卞,齐,康,伍,余,元,卜,顾,孟,平,黄,和,穆,萧,尹,姚,邵,湛,汪,祁,毛,禹,狄,米,贝,明,臧,计,伏,成,戴,谈,宋,茅,庞,熊,纪,舒,屈,项,祝,董,梁,杜,阮,蓝,闵,席,季,麻,强,贾,路,娄,危,江,童,颜,郭,梅,盛,林,刁,钟,徐,邱,骆,高,夏,蔡,田,樊,胡,凌,霍,虞,万,支,柯,昝,管,卢,莫,经,房,裘,缪,干,解,应,宗,丁,宣,贲,邓,郁,单,杭,洪,包,诸,左,石,崔,吉,钮,龚,程,嵇,邢,滑,裴,陆,荣,翁,荀,羊,於,惠,甄,麴,家,封,芮,羿,储,靳,汲,邴,糜,松,井,段,富,巫,乌,焦,巴,弓,牧,隗,山,谷,车,侯,宓,蓬,全,郗,班,仰,秋,仲,伊,宫,宁,仇,栾,暴,甘,钭,厉,戎,祖,武,符,刘,景,詹,束,龙,叶,幸,司,韶,郜,黎,蓟,薄,印,宿,白,怀,蒲,邰,从,鄂,索,咸,籍,赖,卓,蔺,屠,蒙,池,乔,阴,欎,胥,能,苍,双,闻,莘,党,翟,谭,贡,劳,逄,姬'
    arr = str.split(',')
    phoneStartStr = '135、136、137、138、139、150、151、152、157、158、159、187、188、147、130、131、132、156、186、145、133、153、189'
    phoneStartList = phoneStartStr.split('、')
    for i in range(0, 30):
        name = arr[random.randint(0, len(arr) - 1)] + '**'
        phone = phoneStartList[random.randint(0, len(phoneStartList) - 1)] + '****' + randNum() + randNum() + randNum() + randNum()
        str = '<ul style="display: flex;font-size: 2rem;color:#fff"><li style="width: 10rem">' + name + '</li><li style="width: 40rem">' + phone + '</li><li>**区***</li></ul>' + '\n';
        file.write(str)


if __name__ == '__main__':
    main()
