#include <stdlib.h>
#include <stdio.h>

// create three commands
char *cmd1[] = { "/bin/ls", 0 };
char *cmd2[] = { "/bin/wc", "-l", 0 };
char *cmd3[] = { "/bin/ls", "-m", 0 };

void run3com();

int main(int argc, char **argv)
{
	int pid, status;
	int fd[2];

	pipe(fd);
	pid = fork();

	if (pid == 0) {
		run3com(fd);
		exit(0);
	} else if (pid > 0) {
		while ((pid = wait(&status)) != -1)
		 fprintf(stderr, "process %d exits with %d\n", pid, WEXITSTATUS(status));
	} else {
		perror("fork");
		exit(1);
	}
	exit(0);
}


void run3com(int pfd[])
{
	int pid;
	pid = fork();
	if (pid ==0) {
		// fork the child process
		pid = fork();
		if (pid == 0) {
			dup2(pfd[0], 0);
			close(pfd[1]);	
			execvp(cmd3[0], cmd3);
			perror(cmd3[0]);
		} else if (pid > 0) {
			dup2(pfd[0], 0);
			close(pfd[1]);	
			execvp(cmd2[0], cmd2);
			perror(cmd2[0]);
		}
	} else if (pid > 0) {
		dup2(pfd[1], 1);
		close(pfd[0]);	
		execvp(cmd1[0], cmd1);
		perror(cmd1[0]);
	} else {
		perror("fork");
		exit(1);
	}
}
