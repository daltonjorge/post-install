set SYSCIT_JDBC_CONNECTION_STRING jdbc:postgresql://localhost:5432/syscit_prod

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
if test -f /home/dalton/miniconda3/bin/conda
    eval /home/dalton/miniconda3/bin/conda "shell.fish" "hook" $argv | source
end
# <<< conda initialize <<<

source ~/.asdf/asdf.fish

if test -f ~/.asdf/plugins/java/set-java-home.fish
    source ~/.asdf/plugins/java/set-java-home.fish
end

if test -z "$TMUX"
    tmux attach || tmux new-session
else
    tmux switch-client -n
end

# fish_add_path /home/dalton/.local/bin/

set -gx VISUAL nvim
set -gx EDITOR nvim
set -gx DISPLAY :0.0

# fish_config prompt choose nim
# fish_config theme choose tokyonight_night

starship init fish | source
