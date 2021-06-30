from django.http import HttpResponse
from django.shortcuts import render
from .models import HuBeiProvinceHistoryEpidemicData, WuhanPopulationMigrationOut, \
    ProvinceHistoryEpidemicData, WeiBoCommentWordRate, EmotionData, EmotionWordData
import json


def index(request):
    # 读数据库
    hubei_data = list(ProvinceHistoryEpidemicData.objects.filter(province='湖北'))
    national_data_2020 = list(ProvinceHistoryEpidemicData.objects.filter(date=str('12.31')).order_by('province'))
    national_data_2021 = list(
        ProvinceHistoryEpidemicData.objects.filter(date=str('06.21'), year='2021').order_by('province'))
    national_data_2021_ordered = list(
        ProvinceHistoryEpidemicData.objects.filter(date=str('06.21'), year='2021').order_by('-confirm'))

    national_heal_2021_ordered = list(
        ProvinceHistoryEpidemicData.objects.filter(date=str('06.21'), year='2021').order_by('-heal'))[:6]

    national_dead_2021_ordered = list(
        ProvinceHistoryEpidemicData.objects.filter(date=str('06.21'), year='2021').order_by('-dead'))[:6]

    hubei_province = list(HuBeiProvinceHistoryEpidemicData.objects.filter(date='06.09'))

    wuhan_migrate_out = list(WuhanPopulationMigrationOut.objects.all().order_by('-city_rate_out'))[:15]

    emotion_data = list(EmotionData.objects.all())

    # 湖北折线图
    hubei_confirm_list = []
    hubei_dead_list = []
    hubei_heal_list = []
    hubei_date_list = []
    hubei_new_confirm_list = []
    hubei_new_heal_list = []
    hubei_new_dead_list = []
    hubei_province_list = []
    hubei_province_data_list = []

    for hubei in hubei_data:
        hubei_confirm_list.append(hubei.confirm)
        hubei_dead_list.append(hubei.dead)
        hubei_heal_list.append(hubei.heal)
        hubei_date_list.append(hubei.date)
        hubei_new_confirm_list.append(hubei.newConfirm)
        hubei_new_heal_list.append(hubei.newHeal)
        hubei_new_dead_list.append(hubei.newDead)

    for city in hubei_province:
        hubei_province_list.append(city.city)
        hubei_province_data_list.append(city.confirm)

    # 全国疫情数据--->确诊
    national_province_list = []
    national_epidemic_list_2020 = []
    national_epidemic_list_2021 = []
    national_epidemic_ordered_list_2021 = []
    national_epidemic_province_ordered_list_2021 = []

    national_dead_province_2021_list = []
    national_dead_2021_ordered_list = []

    national_heal_province_2021_list = []
    national_heal_2021_ordered_list = []

    for epidemic_data in national_data_2020:
        national_province_list.append(epidemic_data.province)
        national_epidemic_list_2020.append(epidemic_data.confirm)

    for epidemic_data in national_data_2021:
        national_epidemic_list_2021.append(epidemic_data.confirm)

    for city in national_data_2021_ordered:
        national_epidemic_province_ordered_list_2021.append(city.province)
        national_epidemic_ordered_list_2021.append(city.confirm)

    for heal in national_heal_2021_ordered:
        national_heal_2021_ordered_list.append(heal.heal)
        national_heal_province_2021_list.append(heal.province)

    for dead in national_dead_2021_ordered:
        national_dead_2021_ordered_list.append(dead.dead)
        national_dead_province_2021_list.append(dead.province)

    wuhan_migrate_out_city_list = []
    wuhan_migrate_out_rate_list = []

    for rate in wuhan_migrate_out:
        wuhan_migrate_out_rate_list.append(rate.city_rate_out)
        wuhan_migrate_out_city_list.append(rate.city_name)

    positive_sum = 0
    middle_sum = 0
    negative_sum = 0

    for i in emotion_data:
        positive_sum = i.positive_sum
        middle_sum = i.middle_sum
        negative_sum = i.negative_sum

    context = {
        'hubei_confirm_list': json.dumps(hubei_confirm_list),
        'hubei_date_list': json.dumps(hubei_date_list),
        'hubei_heal_list': json.dumps(hubei_heal_list),
        'hubei_dead_list': json.dumps(hubei_dead_list),
        'hubei_new_confirm_list': hubei_new_confirm_list,
        'hubei_new_heal_list': hubei_new_heal_list,
        'hubei_new_dead_list': hubei_new_dead_list,

        'national_epidemic_list_2020': json.dumps(national_epidemic_list_2020),
        'national_epidemic_list_2021': json.dumps(national_epidemic_list_2021),
        'national_province_list': national_province_list,

        'national_epidemic_province_ordered_list_2021': json.dumps(national_epidemic_province_ordered_list_2021),
        'national_epidemic_ordered_list_2021': json.dumps(national_epidemic_ordered_list_2021),

        'national_dead_province_2021_list': national_dead_province_2021_list,
        'national_dead_2021_ordered_list': national_dead_2021_ordered_list,

        'national_heal_province_2021_list': national_heal_province_2021_list,
        'national_heal_2021_ordered_list': national_heal_2021_ordered_list,

        'hubei_province_list': hubei_province_list,
        'hubei_province_data_list': hubei_province_data_list,

        'wuhan_migrate_out_city_list': wuhan_migrate_out_city_list,
        'wuhan_migrate_out_rate_list': wuhan_migrate_out_rate_list,

        'positive_sum': positive_sum,
        'middle_sum': middle_sum,
        'negative_sum': negative_sum,
    }

    return render(request, 'charts/index.html', context)


def detail(request, id):
    hubei_data = list(ProvinceHistoryEpidemicData.objects.filter(province='湖北'))
    national_data_2020 = list(ProvinceHistoryEpidemicData.objects.filter(date=str('12.31')).order_by('province'))
    national_data_2021 = list(
        ProvinceHistoryEpidemicData.objects.filter(date=str('06.21'), year='2021').order_by('province'))
    national_data_2021_ordered = list(
        ProvinceHistoryEpidemicData.objects.filter(date=str('06.21'), year='2021').order_by('-confirm'))

    national_heal_2021_ordered = list(
        ProvinceHistoryEpidemicData.objects.filter(date=str('06.21'), year='2021').order_by('-heal'))[:6]

    national_dead_2021_ordered = list(
        ProvinceHistoryEpidemicData.objects.filter(date=str('06.21'), year='2021').order_by('-dead'))[:6]

    hubei_province = list(HuBeiProvinceHistoryEpidemicData.objects.filter(date='06.09'))

    wuhan_migrate_out = list(WuhanPopulationMigrationOut.objects.all().order_by('-city_rate_out'))[:20]
    wuhan_migrate_in = list(WuhanPopulationMigrationOut.objects.all().order_by('-city_rate_in'))[:20]

    emotion_data = list(EmotionData.objects.all())

    # 湖北折线图
    hubei_confirm_list = []
    hubei_dead_list = []
    hubei_heal_list = []
    hubei_date_list = []
    hubei_new_confirm_list = []
    hubei_new_heal_list = []
    hubei_new_dead_list = []
    hubei_province_list = []
    hubei_province_data_list = []

    for hubei in hubei_data:
        hubei_confirm_list.append(hubei.confirm)
        hubei_dead_list.append(hubei.dead)
        hubei_heal_list.append(hubei.heal)
        hubei_date_list.append(hubei.date)
        hubei_new_confirm_list.append(hubei.newConfirm)
        hubei_new_heal_list.append(hubei.newHeal)
        hubei_new_dead_list.append(hubei.newDead)

    for city in hubei_province:
        hubei_province_list.append(city.city)
        hubei_province_data_list.append(city.confirm)

    # 全国疫情数据--->确诊
    national_province_list = []
    national_epidemic_list_2020 = []
    national_epidemic_list_2021 = []
    national_epidemic_ordered_list_2021 = []
    national_epidemic_province_ordered_list_2021 = []

    national_dead_province_2021_list = []
    national_dead_2021_ordered_list = []

    national_heal_province_2021_list = []
    national_heal_2021_ordered_list = []

    for epidemic_data in national_data_2020:
        national_province_list.append(epidemic_data.province)
        national_epidemic_list_2020.append(epidemic_data.confirm)

    for epidemic_data in national_data_2021:
        national_epidemic_list_2021.append(epidemic_data.confirm)

    for city in national_data_2021_ordered:
        national_epidemic_province_ordered_list_2021.append(city.province)
        national_epidemic_ordered_list_2021.append(city.confirm)

    for heal in national_heal_2021_ordered:
        national_heal_2021_ordered_list.append(heal.heal)
        national_heal_province_2021_list.append(heal.province)

    for dead in national_dead_2021_ordered:
        national_dead_2021_ordered_list.append(dead.dead)
        national_dead_province_2021_list.append(dead.province)

    wuhan_migrate_out_city_list = []
    wuhan_migrate_out_rate_list = []

    for rate in wuhan_migrate_out:
        wuhan_migrate_out_rate_list.append(rate.city_rate_out)
        wuhan_migrate_out_city_list.append(rate.city_name)

    wuhan_migrate_in_city_list = []
    wuhan_migrate_in_rate_list = []

    for rate in wuhan_migrate_in:
        wuhan_migrate_in_rate_list.append(rate.city_rate_in)
        wuhan_migrate_in_city_list.append(rate.city_name)


    positive_sum = 0
    middle_sum = 0
    negative_sum = 0

    for i in emotion_data:
        positive_sum = i.positive_sum
        middle_sum = i.middle_sum
        negative_sum = i.negative_sum

    context = {
        'hubei_confirm_list': json.dumps(hubei_confirm_list),
        'hubei_date_list': json.dumps(hubei_date_list),
        'hubei_heal_list': json.dumps(hubei_heal_list),
        'hubei_dead_list': json.dumps(hubei_dead_list),
        'hubei_new_confirm_list': hubei_new_confirm_list,
        'hubei_new_heal_list': hubei_new_heal_list,
        'hubei_new_dead_list': hubei_new_dead_list,

        'national_epidemic_list_2020': json.dumps(national_epidemic_list_2020),
        'national_epidemic_list_2021': json.dumps(national_epidemic_list_2021),
        'national_province_list': national_province_list,

        'national_epidemic_province_ordered_list_2021': json.dumps(national_epidemic_province_ordered_list_2021),
        'national_epidemic_ordered_list_2021': json.dumps(national_epidemic_ordered_list_2021),

        'national_dead_province_2021_list': national_dead_province_2021_list,
        'national_dead_2021_ordered_list': national_dead_2021_ordered_list,

        'national_heal_province_2021_list': national_heal_province_2021_list,
        'national_heal_2021_ordered_list': national_heal_2021_ordered_list,

        'hubei_province_list': hubei_province_list,
        'hubei_province_data_list': hubei_province_data_list,
        'id': id,

        'wuhan_migrate_out_city_list': wuhan_migrate_out_city_list,
        'wuhan_migrate_out_rate_list': wuhan_migrate_out_rate_list,

        'wuhan_migrate_in_city_list': wuhan_migrate_in_city_list,
        'wuhan_migrate_in_rate_list': wuhan_migrate_in_rate_list,

        'positive_sum': positive_sum,
        'middle_sum': middle_sum,
        'negative_sum': negative_sum,
    }
    return render(request, 'charts/page/index.html', context)


def wordcloud(request):
    word_num_data = list(WeiBoCommentWordRate.objects.filter())

    positive_word_data = list(EmotionWordData.objects.filter(kind=1).order_by('-num'))[:50]
    middle_word_data = list(EmotionWordData.objects.filter(kind=0).order_by('-num'))[:50]
    negative_word_data = list(EmotionWordData.objects.filter(kind=-1).order_by('-num'))[:50]

    word_list = []
    num_list = []

    for word in word_num_data:
        word_list.append(word.word)
        num_list.append(word.num)

    positive_word_data_list = []
    positive_word_num_list = []

    middle_word_data_list = []
    middle_word_num_list = []

    negative_word_data_list = []
    negative_word_num_list = []

    for word in positive_word_data:
        positive_word_data_list.append(word.word)
        positive_word_num_list.append(word.num)

    for word in middle_word_data:
        middle_word_data_list.append(word.word)
        middle_word_num_list.append(word.num)

    for word in negative_word_data:
        negative_word_data_list.append(word.word)
        negative_word_num_list.append(word.num)

    context = {
        'word_list': word_list,
        'num_list': num_list,

        'positive_word_data_list': positive_word_data_list,
        'positive_word_num_list': positive_word_num_list,
        'middle_word_data_list': middle_word_data_list,
        'middle_word_num_list': middle_word_num_list,
        'negative_word_data_list': negative_word_data_list,
        'negative_word_num_list': negative_word_num_list,
    }
    return render(request, 'charts/wordcloud.html', context)
