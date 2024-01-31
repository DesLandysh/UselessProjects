#include <stdio.h>

int main(void){
  
  printf("\e[37;44;0m \\e44bg;37fg;0-reset \033[0m \n");
  printf("\e[37;44;1m \\e44bg;37fg;1-bold \033[0m \n");
  printf("\e[37;44;2m \\e44bg;37fg;2-dim \033[0m \n");
  printf("\e[37;44;3m \\e44bg;37fg;3-intalic \033[0m \n");
  printf("\e[37;44;4m \\e44bg;37fg;4-underline \033[0m \n");
  
  printf("\e[37;44;5m \\e44bg;37fg;5-slow blink \033[0m \n");
  printf("\e[37;44;6m \\e44bg;37fg;6-rapid blink \033[0m \n");
  printf("\e[37;44;7m \\e44bg;37fg;7-reverse fg/bg \033[0m \n");
  
  printf("\e[37;44;8m \\e44bg;37fg;8-hide \033[0m \n");
  printf("\e[37;44;9m \\e44bg;37fg;9-crossed-out \033[0m \n");
  printf("\e[37;44;20m \\e44bg;37fg;20-gothic \033[0m \n");
  
  puts("\n");
  puts("for numbers after 38/48;5;XXX see console_colors.png or list below");  
  printf("\e[38;5;99m \\e[38;5;99m \033[0m \n");
  printf("\e[48;5;99m \\e[38;5;99m \033[0m \n");
  
  puts("\nFONTS\n");
  printf("\e[10m \\e[10m standart font \033[0m \n");
  for (int i = 11; i < 20; ++i){
    printf("\e[%im \\e[%im alternative font \e[0m \n", i, i);
  }
    
  /*
  
  # cursor positioning
ESC [ y;x H     # position cursor at x across, y down
ESC [ y;x f     # position cursor at x across, y down
ESC [ n A       # move cursor n lines up
ESC [ n B       # move cursor n lines down
ESC [ n C       # move cursor n characters forward
ESC [ n D       # move cursor n characters backward
  
  */
  
  puts("\n");
  
  /*40-49 bg. 30-39 fg */
  printf("\033[0;31m DARK RED\t\tforeground \033[0m \n");
  printf("\e[0;32m DARK GREEN\t\tforeground \033[0m \n");
  printf("\033[2;32m 2; GREEN\t\tforeground \033[0m \n");
  printf("\033[22;32m 22; GREEN\t\tforeground \033[0m \n");
  printf("\033[0;33m DARK YELLOW\t\tforeground \033[0m \n");
  printf("\033[0;34m DARK BLUE\t\tforeground \033[0m \n");
  printf("\033[0;35m PURPLE\t\t\tforeground \033[0m \n");
  printf("\033[0;36m OCEAN BLUE\t\tforeground \033[0m \n");
  printf("\033[0;37m GRAY\t\t\tforeground \033[0m \n");
  printf("\033[0m RESET: \\e[0m \033[0m \n");
  
  puts("\n");
  
  printf("\033[1;31m 1;bright RED\t\tforeground \033[0m \n");
  printf("\033[1;32m 1;bright GREEN\t\tforeground \033[0m \n");
  printf("\033[1;33m 1;YELLOW\t\tforeground \033[0m \n");
  printf("\033[1;34m 1;BLUE\t\t\tforeground \033[0m \n");
  printf("\033[1;35m 1;MAGENTA\t\tforeground \033[0m \n");
  printf("\033[1;36m 1;CYAN\t\t\tforeground \033[0m \n");
  printf("\033[1;37m 1;WHITE\t\tforeground \033[0m \n");
    
  puts("\n");
  
  printf("\033[0;41m Hello World. \033[0m \n");
  printf("\033[0;42m Hello World. \033[0m \n");
  printf("\033[0;43m Hello World. \033[0m \n");
  printf("\033[0;44m Hello World. \033[0m \n");
  printf("\033[0;45m Hello World. \033[0m \n");
  printf("\033[0;46m Hello World. \033[0m \n");
  printf("\033[0;47;30m Hello World. \033[0m \n");
  
  puts("\n");
  
  printf("\033[1;41m Hello World. \033[0m \n");
  printf("\033[1;42m Hello World. \033[0m \n");
  printf("\033[1;43m Hello World. \033[0m \n");
  printf("\033[1;44m Hello World. \033[0m \n");
  printf("\033[1;45m Hello World. \033[0m \n");
  printf("\033[1;46m Hello World. \033[0m \n");
  printf("\033[1;47;30m Hello World. \033[0m \n");
 

  char fg[6] = "38;5;";
  char bg[6] = "48;5;";
  for (int mode = 0; mode < 256; ++mode){
    printf("\e[%s%im %4d\e[m", fg, mode, mode);
    if (mode % 8 ==0) puts("\n");
    if (mode > 255) break;
  }
  for (int mode = 0; mode < 256; ++mode){
    printf("\e[%s%im %4d\e[m", bg, mode, mode);
    if (mode % 8 ==0) puts("\n");
    if (mode > 255) break;
  }
  
  return 0;
}