# Deregister and cleanup OpsWorks metadata from EC2 instance

sudo /etc/init.d/monit stop
sudo /etc/init.d/opsworks-agent stop
sudo rm -rf /etc/aws/opsworks/ /opt/aws/opsworks/ /var/log/aws/opsworks/ /var/lib/aws/opsworks/ /etc/monit.d/opsworks-agent.monitrc /etc/monit/conf.d/opsworks-agent.monitrc /var/lib/cloud/
yum remove opsworks-agent-ruby-2.2.3-1.x86_64 -y
