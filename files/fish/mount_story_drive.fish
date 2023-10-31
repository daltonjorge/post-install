function mount_story_drive --description 'Mount story drive with write permission'
  sudo mount -o remount,rw,force /dev/sdb1
end

