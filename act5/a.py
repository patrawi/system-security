def main():
    cypherText = 'PRCSOFQX FP QDR AFOPQ CZSPR LA JFPALOQSKR. QDFP FP ZK LIU BROJZK MOLTROE.'
    count = dict()
    for e in cypherText:
        if (e != '.') and (e != ' '):
            if e not in count:
                count[e] = 1
            else:
                count[e] += 1
    print(count)


if __name__ == '__main__':
    main()
