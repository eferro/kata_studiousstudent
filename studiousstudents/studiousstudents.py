import copy


class StudiousStudentsSorter(object):
    def sort(self, inputline):
        words = inputline.split()[1:]
        return ''.join(self._sort_tokens(words))

    def sort_file(self, path):
        for line in open(path).readlines()[1:]:
            print self.sort(line)



    def _sort_tokens(self, remaining):
        if not remaining:
            return []

        candidates = {}
        for index, word in enumerate(remaining):
            candidates[word] = ''.join(self._sort_tokens(self._list_without_element(remaining, index)))

        return sorted([ k+v for k,v in candidates.iteritems()])[0]

    def _list_without_element(self, l, index):
        newlist = copy.copy(l)
        del newlist[index]
        return newlist

if __name__ == '__main__':
    import sys
    StudiousStudentsSorter().sort_file(sys.argv[1])