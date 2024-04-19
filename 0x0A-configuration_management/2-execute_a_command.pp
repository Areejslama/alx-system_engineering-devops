# this script create a manifest that kills
exec { ' kill_killmenow_process':
command => 'pkill killmenow',
path    => '/bin:/usr/bin', 
}
