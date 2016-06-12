/etc/rsyncd.conf:
motd file = /etc/rsyncd.motd
log file = /var/log/rsyncd.log
pid file = /var/run/rsyncd.pid
lock file = /var/run/rsync.lock

[honor]
   path = /home/honor/tmp/update
   comment = Honor Local Rsync Server By Mixed_kr
   uid = honor
   gid = honor
   read only = yes
   list = yes
   hosts allow = 10.0.0.0/24 10.0.1.0/24 10.0.2.0/24 10.0.3.0/24      
   hosts deny = *
   auth users = honor
   ignore errors = yes 
   secrets file = /etc/rsyncd.secrets
   
   
/etc/rsyncd.secrets:
1234abcd

/etc/rsyncd.motd:
Honor Local Rsync Server By Mixed_kr



yum install xinetd -y
# vim /etc/xinetd.d/rsync
建立一个名为/etc/xinetd.d/rsync文件，输入以下内容：
service rsync
{
         disable = no
         socket_type　　= stream
         wait　　　　　 = no
         user　　　　　 = root
         server　　　　 = /usr/local/rsync/bin/rsync
         server_args　　= –daemon
         log_on_failure += USERID
}
/etc/init.d/xinetd reload

chmod 600 /etc/rsyncd.secrets
