#!/bin/bash

if [ $EUID -eq 0 ]; then
    echo -n "Вы запустили программу от суперпользователя, вы уверены что хотите продолжить? [д/Н]: "
    read -r userPrikolist;
    if [ "$userPrikolist" != "д" ]; then
        exit 1
    fi
fi

pr_list() {
    if [ "$1" == "work" ] ; then
        echo "Список расширений рабочих файлов: "
        list="$work_file"
    elif [ "$1" == "temp" ] ; then
        echo "Список расширений временных файлов: "
        list="$temp_file"
    fi
  
    set -f
    for i in $list ; do
        echo "$i"
    done
    set +f
    }


make_list() {
    if [ "$1" == "work" ] ; then
        echo -n "Введите количество расширений рабочих файлов: "
        read -r amount
    elif [ "$1" == "temp" ] ; then
        echo -n "Введите количество расширений временных файлов: "
        read -r amount
    fi
    list=""
    set -f
    while [ "$amount" -gt 0 ] ; do
        echo -n "Введите расширение в виде '*.расширение': "
        read -r extension
        if echo "$extension" | grep -Eq "^\*\.[A-Za-z0-9]+$" ; then
            list+=" $extension"
            amount=$((amount - 1))
        else
            echo "Неверный формат расширения."
        fi
    done
    set +f
    if [ "$1" == "work" ] ; then
        work_file="$list"
    elif [ "$1" == "temp" ] ; then
        temp_file="$list"
    fi
    write_config
    }


append_list() {
    set -f
    echo -n "Введите расширение в виде '*.расширение': "
    read -r extension
    if echo "$extension" | grep -Eq "^\*\.[A-Za-z0-9]+$" ; then
        if [ "$1" == "work" ] ; then
            work_file+=" $extension"
        elif [ "$1" == "temp" ] ; then
            temp_file+=" $extension"
        fi
    else
        echo "Неверный формат расширения."
    fi
    set +f
    write_config
    }


del_list() {
    set -f
    echo -n "Введите номер удаляемого расширения: "
    read -r number
    if echo "$number" | grep -Eq "^[1-9][0-9]*$" ; then
        counter=1
        list=''
        if [ "$1" == "work" ] ; then
            for i in $work_file ; do
                if [ "$counter" -ne "$number" ] ; then
                    list+=" $i"
                fi
                counter=$((counter + 1))
            done
            work_file="$list"
        elif [ "$1" == "temp" ] ; then
            for i in $temp_file ; do
                if [ "$counter" -ne "$number" ] ; then
                    list+=" $i"
                fi
                counter=$((counter + 1))
            done
            temp_file="$list"
        fi
    else
        echo "Неверный номер."
    fi
    set +f
    write_config
    }


make_folder() {
    echo -n "Введите новую папку: "
    read -r folder
    IFS_old="$IFS"
    IFS=''
    if [ -d "$folder" ] ; then
        work_folder="$folder"
        cd "$folder"
    else
        echo "Несуществующая папка."
    fi
    IFS="$IFS_old"
    write_config
    }


del_temp() {
    for i in $temp_file ; do
        file="./$i"
        if [ -f "$file" ] ; then
            rm -f "$file"
        fi
    done
    }


make_command() {
    echo -n " Введите команду: "
    read -r command
    if [ -n "$command" ] ; then
        written_command="$command"
        write_config
    else
        echo "Пустая строка."
    fi
    }

pr_strings() {
    for i in $work_file ; do
        file="./$i"
        echo " $file:"
        if [ -f "$file" ] ; then
            grep -Eo "'.*'" "$file"
        fi
    done
    }


pr_sizes() {
    for i in $temp_file ; do
        file="./$i"
        if [ -f "$file" ] ; then
            du -h "$file"
        fi
    done
    }


make_temp_silent() {
    set -f
    list=''
    for i in "$@" ; do
        if echo "$i" | grep -Eq "^\*\.[A-Za-z0-9]+$" ; then
            list+=" $i"
        fi
    done
    if [ -n "$list" ] ; then
        temp_file="$list"
        write_config
    fi
    set +f
    }
    

make_work_silent() {
    set -f
    list=''
    for i in "$@" ; do
        if echo "$i" | grep -Eq "^\*\.[A-Za-z0-9]+$" ; then
            list+=" $i"
        fi
    done
    if [ -n "$list" ] ; then
        work_file="$list"
        write_config
    fi
    set +f
    }

append_silent() {
    if echo "$1" | grep -Eq "^\*\.[A-Za-z0-9]+$" ; then
        if [ "$2" == "work" ] ; then
            work_file+=" $extension"
        elif [ "$2" == "temp" ] ; then
            temp_file+=" $extension"
        fi
    fi
    set +f
    write_config
    }


del_silent() {
    if echo "$1" | grep -Eq "^[1-9][0-9]*$" ; then
        counter=1
        list=''
        if [ "$2" == "work" ] ; then
            for i in $work_file ; do
                if [ "$counter" -ne "$number" ] ; then
                    list+=" $i"
                fi
                counter=$((counter + 1))
            done
            work_file="$list"
        elif [ "$2" == "temp" ] ; then
            for i in $temp_file ; do
                if [ "$counter" -ne "$number" ] ; then
                    list+=" $i"
                fi
                counter=$((counter + 1))
            done
            temp_file="$list"
        fi
    fi
    write_config
    }


make_folder_silent() {
    IFS_old="$IFS"
    IFS=""
    if [ -d "$1" ] ; then   
        work_folder="$1"
    fi
    write_config
    
    cd "$work_folder"
    pwd
    IFS="$IFS_old"
    }


make_command_silent() {
    if [ -n "$1" ] ; then
        written_command="$1"
        write_config
    fi
    }


make_config() {
    config="$(dirname "$0")/.myconfig"
    echo "*.log" >> "$config"
    echo "*.py" >> "$config"
    dirname "$0" >> "$config"
    echo "grep def* program.py >last.log" >> "$config"
    }


write_config() {
    config="$(dirname "$0")/.myconfig"
    echo "$config"
    echo "$temp_file" > "$config"
    echo "$work_file" >> "$config"
    echo "$work_folder" >> "$config"
    echo "$written_command" >> "$config"
    }


read_config() {
    config="$(dirname "$0")/.myconfig"
    #echo "$config"
    temp_file=$(head -n 1 "$config" | tail -n 1)
    work_file=$(head -n 2 "$config" | tail -n 1)
    work_folder=$(head -n 3 "$config" | tail -n 1)
    IFS_old="$IFS"
    IFS=""
    cd "$work_folder"
    IFS="$IFS_old"
    written_command=$(head -n 4 "$config" | tail -n 1)
    }




config="$(dirname "$0")/.myconfig"
if [ -f "$config" ] ; then
    read_config
else
    make_config
    read_config
fi

if [ "$1" != -s ] ; then
    menu_number=1
    while [ "$menu_number" != "0" ] ; do
        echo "1. Просмотреть список расширений временных файлов
2. Задать заново список расширений временных файлов
3. Добавить расширение в список расширений временных файлов
4. Удалить расширение из списка расширений временных файлов
5. Просмотреть список расширений рабочих файлов
6. Задать заново список расширений рабочих файлов
7. Добавить элемент в список расширений рабочих файлов
8. Удалить элемент из списка расширений рабочих файлов
9. Просмотреть рабочую папку скрипта
10. Задать заново рабочую папку скрипта
11. Удалить временные файлы
12. Выполнить записанную команду
13. Просмотреть записанную команду
14. Изменить записанную команду
15. Просмотреть все строки, ограниченные апострофами во всех рабочих файлах
16. Просмотреть объём каждого временного файла
0. Завершить скрипт"
        echo -n "Выберите пункт меню (от 0 до 14): "
        read -r menu_number
        
        if [ "$menu_number" == "1" ] ; then
            pr_list temp
        elif [ "$menu_number" == "2" ] ; then
            make_list temp
        elif [ "$menu_number" == "3" ] ; then
            append_list temp
        elif [ "$menu_number" == "4" ] ; then
            del_list temp
        elif [ "$menu_number" == "5" ] ; then
            pr_list work
        elif [ "$menu_number" == "6" ] ; then
            make_list work
        elif [ "$menu_number" == "7" ] ; then
            append_list work
        elif [ "$menu_number" == "8" ] ; then
            del_list work
        elif [ "$menu_number" == "9" ] ; then
            echo "$work_folder"
        elif [ "$menu_number" == "10" ] ; then
            make_folder
        elif [ "$menu_number" == "11" ] ; then
            del_temp
        elif [ "$menu_number" == "12" ] ; then
            eval "$written_command"
        elif [ "$menu_number" == "13" ] ; then
            echo "$written_command"
        elif [ "$menu_number" == "14" ] ; then
            make_command
        elif [ "$menu_number" == "15" ] ; then
            pr_strings
        elif [ "$menu_number" == "16" ] ; then
            pr_sizes
        fi
    done
else
    if [ "$2" == "prwrk" ] ; then
        pr_list work
    
    elif [ "$2" == "prtmp" ] ; then
        pr_list temp
    
    elif [ "$2" == "mktmp" ] ; then
        shift
        shift
        extensions=''
        for i in "$@" ; do
            extensions+=" $i"
        done
        make_temp_silent $extensions
    
    elif [ "$2" == "mkwrk" ] ; then
        shift
        shift
        extensions=''
        for i in "$@" ; do
            extensions+=" $i"
        done
        make_work_silent $extensions
    
    elif [ "$2" == "addtmp" ] ; then
        append_silent "$3" temp
    
    elif [ "$2" == "addwrk" ] ; then
        append_silent "$3" work
    
    elif [ "$2" == "deltmp" ] ; then
        del_silent "$3" temp
    
    elif [ "$2" == "delwrk" ] ; then
        del_silent "$3" work
    
    elif [ "$2" == "prfolder" ] ; then
        echo "$work_folder"
        pwd
    
    elif [ "$2" == "mkfolder" ] ; then
        shift
        shift
        dir=''
        for i in "$@" ; do
            dir+=" $i"
        dir="${dir:1}"
        done
        make_folder_silent "$dir"
    
    elif [ "$2" == "delfiles" ] ; then
        del_temp
    
    elif [ "$2" == "execcmd" ] ; then
        eval "$written_command"
    
    elif [ "$2" == "prcmd" ] ; then
        echo "$written_command"
    
    elif [ "$2" == "mkcmd" ] ; then
        make_command_silent "$3"
    
    elif [ "$2" == "prstr" ] ; then
        pr_strings
    
    elif [ "$2" == "prsizes" ] ; then
        pr_sizes
    fi
fi
exit
