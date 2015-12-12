from subprocess import check_output

CMD_REMOTE_V = "git remote -v".split()
def main():
    remote_v_out = check_output(CMD_REMOTE_V)
    remote_url = get_remote(remote_v_out)
    print remote_url


def get_remote(remote_v_out):
    git_remote = remote_v_out.split()[1]
    return git_remote

def set_remote(remote_name,remote_url):
    pass

if __name__ == '__main__':
    print "Running"
    main()
