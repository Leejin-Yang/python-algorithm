def solution(sizes):
    answer = 0
    
    for i in sizes:
        i.sort()
    
    m_width = max(size[0] for size in sizes)
    m_height = max(size[1] for size in sizes)
    
    answer = m_width * m_height
    return answer