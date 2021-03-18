
n = ['a','b','c','d','e']
m = ['f','g','h','c','i']

def has_common_elements(n, m):
    m_dict = dict(zip(m,m))
    for val in n:
        # dict lookups are O(1)
        if val in m_dict:
            return True
        
    return False

if __name__ == '__main__':
    print(has_common_elements(n, m))