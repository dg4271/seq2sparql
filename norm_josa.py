# -*- coding: utf-8 -*- 

# https://github.com/letsgo247/under-checker
# 아스키(ASCII) 코드 공식에 따라 입력된 단어의 마지막 글자 받침 유무를 판단해서 뒤에 붙는 조사를 리턴하는 함수
def normalize_josa(s, label):    
    # find josa
    josa_idx = s.find(label)+len(label)
    josa = s[josa_idx:].split(' ')[0]
    josa = re.sub('[?]', '', josa).strip()

    no_under = [u"는", u"가", u"를", u"와", u"야", u"여", u"랑"]
    with_under = [u"은", u"이", u"을", u"과", u"아", u"이여", u"이랑"]
    under_swap_dic = {}
    for no_j, with_j in zip(no_under, with_under):
        under_swap_dic[no_j] = with_j
        under_swap_dic[with_j] = no_j

    last = unicode(label.decode('UTF-8'))[-1]  
    criteria = (ord(last) - 44032) % 28  #아스키(ASCII) 코드 공식에 따라 계산 (계산법은 다음 포스팅을 참고하였습니다 : http://gpgstudy.com/forum/viewtopic.php?p=45059#p45059)
    
    if criteria == 0: #나머지가 0이면 받침이 없는 것
        if josa in no_under: return s 
        elif josa in under_swap_dic.keys(): return s[:josa_idx] + under_swap_dic[josa] + s[josa_idx+len(josa):]
    else: #나머지가 0이 아니면 받침 있는 것                 
        if josa in with_under: return s 
        elif josa in under_swap_dic.keys(): return s[:josa_idx] + under_swap_dic[josa] + s[josa_idx+len(josa):]

    return s

if __name__ == '__main__':
    print normalize_josa("허들는 나다", "허들")
    print normalize_josa("허들은 나다", "허들")
    
    print normalize_josa("허드서커는 나다", "허드서커")
    print normalize_josa("허드서커은 나다", "허드서커")



    
    
