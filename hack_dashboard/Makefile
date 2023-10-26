# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bsilva-c <bsilva-c@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/15 21:55:39 by bsilva-c          #+#    #+#              #
#    Updated: 2023/09/15 22:46:45 by bsilva-c         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

all: up
build:
	@sudo mkdir -p /var/lib/mongodb_data
	sudo docker compose -f ./srcs/docker-compose.yml build --no-cache
up: build
	sudo docker compose -f ./srcs/docker-compose.yml up -d --no-build
down:
	sudo docker compose -f ./srcs/docker-compose.yml down
start:
	sudo docker compose -f ./srcs/docker-compose.yml start
stop:
	sudo docker compose -f ./srcs/docker-compose.yml stop
ps:
	sudo docker compose -f ./srcs/docker-compose.yml ps
rm: stop
	sudo docker compose -f ./srcs/docker-compose.yml rm
delete_volumes:
	sudo docker compose -f ./srcs/docker-compose.yml down --volumes
	# @sudo rm -rf /var/lib/mongodb_data
system_prune:
	sudo docker system prune
re: fclean all ps
clean: stop rm
fclean: stop rm delete_volumes system_prune
