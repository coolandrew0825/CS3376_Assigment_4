// name: Andrew Chen
// class: CS 3376
// date: 12.5.16

#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main(int argc, char **argv)
{
	int pid, status;
	int fdout;	/* new file descriptor for output */
	char *command[] = { "ls", "-l", ">", "output.txt" };

	if ((fdout = open(command[3], O_CREAT|O_TRUNC|O_WRONLY, 0644)) < 0) {
		perror(command[3]);	/* open failed */
		exit(1);
	}
	printf("writing output of the command %s to \"%s\"\n", command[0], command[3]);

	dup2(fdout, 1); 
	execlp(command[0], command[0], command[1], (char *)0);

	perror(command[0]);		/* execvp failed */
	exit(1);
}

void redirection(int pfd[])
{
	int pid;
	pid = fork();
	// checking if the string contains < and output.txt
	if (command[2] == "<" && command[3] = "output.txt") {
		fid = open(filename, O_RDONLY);
		close(STD_INPUT);
		dup(fid);
		close(fid);
	} else {
		perror("fork");
		exit(1);
	}
}