# CTF 1 - 2nd June

## Try It Out

Just copied the flag from the prompt and pasted it :).

## Welcome Agent

- SSH (Secure Shell) usage: `ssh username@host -p port`

- Following the prompt, typed this into my Kali-linux terminal:
  ```sh
  ssh ctfuser@3.7.66.170 -p 2201
  password: ctfpassword
  ```
- Then to view the files in the current directory: `ls` (list).
- Found `flag.txt` and viewed its contents using `cat flag.txt` (concatenate) to find the flag.

## Hidden in the Crowd

- SSHed into the target:
  ```sh
  ssh ctfuser@3.7.66.170 -p 2211
  password: ctfpassword
  ```
- To view the hidden files: `ls -la` where the options
  `-l` stands for detailed listing and `-a` stands for all (hidden files too)
- Found the file `.flag` and `cat`-ed it to find the flag.

## Log Explore

- Downloaded the logGen file and ran it using `./logGen` to generate a 16GB `log.txt` file (even Notepad gave up trying to open it).

- Tried `grep "{.*} log.txt"` to match curly braces format of the flag but met with `grep: log.txt: binary file matches`.

- After a bit of googling, added the `--binary-files=text` flag to the command to treat the file as text even though it contained binary characters.
  Finally found this: `!! ALERT: hidden flag --> dcCTF{b1G_L0g}`

## Process Hunter

- SSHed into the target:

  ```sh
  ssh ctfuser@3.7.66.170 -p {port}
  password: ctfpassword
  ```

- To see the processes then `ps -aux` where `ps` stands for process status and flags where the flag `-a` shows it for all users, `-u` shows the output in user format and `-x` shows processes not attached to a terminal.

- Located the program running and saw the flags with which it was running revealing the flag.

## Bring Back from the Dead

- First downloaded the `challenge.img` file and mounted it onto a folder using `sudo mount -o loop challenge.img challenge` where `-o loop` flag allows the disk image file to be loaded with a loopback device, preparing it into a format which `mount` expects.

- Then `cd`-ed and `ls`-ed to reveal a readme hinting that some files had been permanently deleted which had to be recovered.

- Researching a bit about this revealed a GUI software `photorec` suitable for this task which was apparently already installed in Kali Linux.

- Guided by the GUI, recovered 2 image (.png) files which were deleted, opening which revealed the flag.

## Git Gud

- Downloaded and extracted the folder on my local machine.

- Simply opened the folder using VSCode and viewed the git history using the Git extensions ;)

- Found an older commit message revealing the deleted file, which further revealed the flag.

## LockedVault

- Downloaded a tar.gz file and opened it using `tar -xzf {filename}` where `-x` stands for decoding, `-z` to gzip (.gz) and `-f` to state the file name.

- Somehow, the unzipping process broke the permissions on the files and allowed me to simply `cat` the files seeing the underlying bash script after which I simply ran the last password through `base64 -d` to decode it to get the flag.

- I understand the intended solution wanted to use `chmod` to provide read, write and executable permissions to the files using `+r`, `+w` and `+x` flags respectively (but if it works, it works right? ;D).
