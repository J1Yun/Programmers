from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    report_who = defaultdict(set)
    for rep in report:
        id, report_id = rep.split()
        report_who[report_id].add(id)

    restricted_id = []
    for id in id_list:
        if len(report_who[id]) >= k:
            restricted_id.append(id)

    for id in id_list:
        count = 0
        for rid in restricted_id:
            if id in report_who[rid]:
                count += 1
        answer.append(count)
    
    return answer