def main():
    with open('../ca-certificates.cert', 'r') as cert_file:
        # Read the contents of the file
        cert_content = cert_file.readlines()
        cert_num = 0
        # Print the contents of the file
        for e in cert_content:
            if (e == '-----BEGIN CERTIFICATE-----\n'):
                cert_num += 1
        print(cert_num)


if __name__ == '__main__':
    main()
