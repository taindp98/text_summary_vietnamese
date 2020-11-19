from bs4 import BeautifulSoup
import json
import pandas as pd
import re
import json
import numpy as np
from collections import OrderedDict
from pyvi import ViTokenizer
def get_event(doc):
  list_eve = []
  for html in list(doc["html_annotation"]):
    soup = BeautifulSoup(html,'html.parser')
    events = soup.find_all("span", {"class": "tag"})
    for e in events:
      dict_eve = {}
      dict_eve["event_type"] = e["data"]
      dict_eve["event_id"] = e["event_id"]
      dict_eve["text"] = e.text
      list_eve.append(dict_eve)
  return list_eve

def load_jsonfile(path):
    list_data = []
    for line in open(path, 'r'):
        list_data.append(json.loads(line))
    df = pd.DataFrame.from_dict(list_data)
    return df
uniChars = "àáảãạâầấẩẫậăằắẳẵặèéẻẽẹêềếểễệđìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵÀÁẢÃẠÂẦẤẨẪẬĂẰẮẲẴẶÈÉẺẼẸÊỀẾỂỄỆĐÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴÂĂĐÔƠƯ"
unsignChars = "aaaaaaaaaaaaaaaaaeeeeeeeeeeediiiiiooooooooooooooooouuuuuuuuuuuyyyyyAAAAAAAAAAAAAAAAAEEEEEEEEEEEDIIIOOOOOOOOOOOOOOOOOOOUUUUUUUUUUUYYYYYAADOOU"


def loaddicchar():
    dic = {}
    char1252 = 'à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ'.split(
        '|')
    charutf8 = "à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ".split(
        '|')
    for i in range(len(char1252)):
        dic[char1252[i]] = charutf8[i]
    return dic
dicchar = loaddicchar()
def convert_unicode(txt):
    return re.sub(
        r'à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ',
        lambda x: dicchar[x.group()], txt)
def clean_mess(mess):
    # input: câu nhập vào của người dùng
    # return: câu đã loại bỏ special token
    mess_unic = convert_unicode(mess)
    mess_rmspectoken = re.findall(r"(?i)\b[a-záàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđ0-9+-,]+\b", mess_unic)
    mess_add_space = mess_rmspectoken + [' ']
    mess_norm = ' '.join(mess_add_space)
    return mess_norm

# def clean_entity_player_name(mess):
#     # input: câu nhập vào của người dùng
#     # return: câu đã loại bỏ special token
#     mess_unic = convert_unicode(mess).lower()
#     mess_rmspectoken = re.findall(r"(?i)\b[a-záàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđ0-9+-]+\b", mess_unic)
#     # mess_add_space = mess_rmspectoken + [' ']
#     mess_norm = ' '.join(mess_rmspectoken)
#     return mess_norm

def clean_sentence_lstm(mess):
    # input: câu nhập vào của người dùng
    # return: câu đã loại bỏ special token
    mess_unic = convert_unicode(mess)
    mess_rmspectoken = re.findall(r'(?i)\b[a-záàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđ0-9+]+\b', mess_unic)
    mess_norm = ' '.join(mess_rmspectoken)
    return mess_norm
def find_entity_equation(sentence,list_entity):
    #input câu nhập user nhập vào
    #output tất cả các thực thể trong list_entity có trong câu
    normalized_sentence=convert_unicode(sentence)
    list_token_sentence=normalized_sentence.split(' ')
    list_result_entity=[]
    list_normalized_entity=[convert_unicode(entity) for entity in list_entity]
    for entity in list_normalized_entity:
        list_token_entity=entity.split(' ')
        for i in range(len(list_token_sentence)-len(list_token_entity)+1):
            if list_token_entity==list_token_sentence[i:i+len(list_token_entity)]:
                list_result_entity.append(entity)
    return list_result_entity

def longest_common_sublist(a, b):
    #input list a, list b
    #output số item chung liền kề dài nhất và giá trị item đầu tiên trong list item chung
    table = {}
    l = 0
    i_max = None
    j_max = None
    for i, ca in enumerate(a, 1):
        #enumerate(iter,start)
        for j, cb in enumerate(b, 1):
            if ca == cb:
                table[i, j] = table.get((i - 1, j - 1), 0) + 1
                if table[i, j] > l:
                    l = table[i, j]
                    i_max=i
                    j_max=j
    if i_max != None:
        return l,i_max - 1
    return l,i_max

def lcs_length(a, b):
    #input list a, list b
    #output max length cả liền kề / không liền kề
    table = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i, ca in enumerate(a, 1):
        for j, cb in enumerate(b, 1):
            table[i][j] = (
                table[i - 1][j - 1] + 1 if ca == cb else
                max(table[i][j - 1], table[i - 1][j]))
    return table[-1][-1]

def find_entity_longest_common(sentence,list_entity,entity_name):
    #input câu user nhập vào,list entity, entity được chọn để bắt
    #output index của entity bắt được trong list entity, chiều dài max, index last của token match trong câu nhập vào
    normalized_sentence=convert_unicode(sentence).lower()
    list_token_sentence = normalized_sentence.split(' ')
    list_result_entity = []
    dict_max_len = {}
    list_normalized_entity = [str(entity).lower() for entity in list_entity]

    result = []
    longest_common_length = None
    end_common_index = None
    for index, entity in enumerate(list_normalized_entity):
        list_token_entity = entity.split(' ')
        # print(list_token_entity)
        # print(list_token_sentence)
        longest_common_length, end_common_index = longest_common_sublist(list_token_sentence,list_token_entity)
        if longest_common_length!=0:
            dict_max_len[(index)] = {'longest_common_length':longest_common_length,'end_common_index':end_common_index}
        # list_token_sentence = list_token_sentence[: end_common_index - longest_common_length] + list_token_sentence[end_common_index:]
    max_longest_common_length=0
    for k,v in dict_max_len.items():
        if v['longest_common_length']>max_longest_common_length:
            max_longest_common_length=v['longest_common_length']

    for k,v in dict_max_len.items():
        if v['longest_common_length']==max_longest_common_length:
            if entity_name in ['register','reward','works']:
                result.append({"longest_common_entity_index":int(k),"longest_common_length":v['max_length_in_sentence'],"end_common_index":v['end_common_index']})
            else:
                result.append({"longest_common_entity_index":int(k),"longest_common_length":v['longest_common_length'],"end_common_index":v['end_common_index']})
    return result

# def catch_time(input_sentence):
#     time_minute = re.findall(r"\bphút\b\s{1}\d+[+']*\d*\s{1}",input_sentence)
#     if time_minute:
#         res_time = time_minute[0].replace(r'phút',r'').replace(r' ',r'').replace(r"'",r'')
#         return res_time
#     else:
#         time_apostrophe = re.findall(r"\d+[+']+\d*",input_sentence)
#         if time_apostrophe:
#             res_time=str(time_apostrophe[0]).replace(r' ',r'').replace(r"'",r'')
#             return res_time
def catch_time(input_sentence):
    time_minute_single = re.findall(r"\bphút\b\s{1}\d+['+]*\d*[']*",input_sentence)
    time_minute_double = re.findall(r'\bphút\b\s{1}\d+["+]*\d*["]*',input_sentence)
    time_apostrophe_single = re.findall(r"\d+['+]+\d*[']*",input_sentence)
    time_apostrophe_double = re.findall(r'\d+["+]+\d*["]*',input_sentence)
    times = time_minute_single + time_minute_double + time_apostrophe_single + time_apostrophe_double
    list_time = []
    res_time = []
    for time in times:
        if time != '':
            list_time.append(time)
    if len(list_time) != 0:
        for time in list_time:
            norm_time = str(time).replace(r'phút',r'').replace(r' ',r'').replace(r"'",r'').replace(r'"',r'')
            if norm_time not in res_time:
                res_time.append(norm_time)
    return res_time


# print(re.findall(r"\bphút\b\s{1}\d+\s{1}","ronaldo ghi bàn thắng ở phút 90 phạt nâng tỷ số lên thành 2-0 cho real madrid"))
# print(catch_time('ronaldo 4-4-3'))
def catch_score(input_sentence):
    score = re.findall(r'\s{1}\d+[-]+\d+\s{1}',input_sentence)
    if score:
        score_split = score[0].split('-')
    else:
        score_split = [np.int(0),np.int(0)]
    return score_split
text = 'ghi bàn ở đội hình 4-4-2 những phút đầu hiệp 2 nâng tỷ số lên thành'
# print(catch_score(text))
def find_all_entity(input_sentence,dict_entity):
    # clean giu lai 90'
    norm_4_score_time = convert_unicode(input_sentence).replace(r',',r' ') + ' '
    # print('norm_4_score_time',norm_4_score_time)
    result_entity_dict={}
    result_entity_dict['score'] = []
    result_entity_dict['score'] = {'score1':catch_score(norm_4_score_time)[0],'score2':catch_score(norm_4_score_time)[1]}
    result_entity_dict['time'] = []
    result_entity_dict['time'] = catch_time(norm_4_score_time)
    list_order_entity_name = ['team_name','player_name']
    map_entity_name_to_threshold={}
    for entity_name in list_order_entity_name:
        map_entity_name_to_threshold[entity_name]=1

    ordered_real_dict = OrderedDict()
    for entity_name in list_order_entity_name:
        ordered_real_dict[entity_name] = dict_entity[entity_name]
        # print(ordered_real_dict[entity_name])
    for entity_name, list_entity in ordered_real_dict.items():
        # if entity_name == "player_name":
        #     matching_threshold = 0.5
        #     # normalized_input_sentence = clean_mess(input_sentence)
        # else:
        #     matching_threshold = 0.55
        matching_threshold = 0.55
        # normalized_input_sentence = ViTokenizer.tokenize( clean_mess(input_sentence))
        normalized_input_sentence = clean_mess(input_sentence)
        catch_entity_threshold_loop = 0
        # print(normalized_input_sentence)

        while True:
            if catch_entity_threshold_loop > 3:
                break
            list_dict_longest_common_entity = find_entity_longest_common(normalized_input_sentence,list_entity,entity_name)
            if list_dict_longest_common_entity == []:
                break
            if list_dict_longest_common_entity[0]['longest_common_length'] < map_entity_name_to_threshold[entity_name] :
                break

            list_sentence_token = normalized_input_sentence.split(' ')
            greatest_entity_index=None
            greatest_common_length = None
            greatest_end_common_index = None
            max_match_entity = 0.0
            for dict_longest_common_entity in list_dict_longest_common_entity:
                longest_common_entity_index = dict_longest_common_entity['longest_common_entity_index']
                longest_common_length = dict_longest_common_entity['longest_common_length']
                end_common_index = dict_longest_common_entity['end_common_index']
                list_sentence_token_match = list_sentence_token[end_common_index - longest_common_length+1:end_common_index+1]

                list_temp_longest_entity_token = str(list_entity[longest_common_entity_index]).split(' ')
                score = len(list_sentence_token_match)/float(len(list_temp_longest_entity_token))
                # print(score)
                if score > max_match_entity:
                    max_match_entity = score
                    greatest_entity_index = longest_common_entity_index
                    greatest_common_length = longest_common_length
                    greatest_end_common_index = end_common_index
            if greatest_common_length >= map_entity_name_to_threshold[entity_name] and max_match_entity > matching_threshold:
                result = ' '.join(list_sentence_token[greatest_end_common_index - greatest_common_length +1 :greatest_end_common_index +1])

                if entity_name in result_entity_dict:
                    result_entity_dict[entity_name].append(result)
                else:
                    result_entity_dict[entity_name] = [result]
                list_sentence_token[greatest_end_common_index - greatest_common_length +1 :greatest_end_common_index +1] = ["✪"]*greatest_common_length
                normalized_input_sentence = ' '.join(list_sentence_token)
            catch_entity_threshold_loop = catch_entity_threshold_loop + 1

    return result_entity_dict
def load_entity(ENTITY_DATA_PATH):
    # TRAIN_DATA_PATH = f'{DATA_PATH}train.jsonl'
    # ENTITY_DATA_PATH = f'{DATA_PATH}entity.csv'
    file = open(ENTITY_DATA_PATH,'r')
    lines = file.readlines()
    dict_entity = {}
    dict_entity['team_name'] = str(lines[0]).replace(r'[',r'').replace(r']',r'').replace(r"'",r'').replace('\n',r'').split(', ')
    dict_entity['player_name'] = str(lines[1]).replace(r'[',r'').replace(r']',r'').replace(r"'",r'').replace('\n',r'').split(', ')
    return dict_entity
