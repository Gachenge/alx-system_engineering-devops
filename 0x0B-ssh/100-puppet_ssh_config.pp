# code to bypass password
file{ '/home/victor/programming/alx-system_engineering-devops/0x0B-ssh/100-puppet_ssh_config.pp':
owner => 'victor',
group => 'victor',
mode => '0600',
content => "Host ubuntu\n\
            \tIdentityFile ~/.ssh/school\n\
            \tPasswordAuthentication no\n",
}
