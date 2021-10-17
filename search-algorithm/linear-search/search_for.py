from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 값이 같은 원소를 선형 검색 (for 문)"""
    for i in range(len(a)):
        if a[i] == key:
            return i
        return -1