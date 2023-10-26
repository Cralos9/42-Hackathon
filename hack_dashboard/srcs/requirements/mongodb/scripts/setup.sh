#!/bin/bash

# Start MongoDB in the background
mkdir -p /var/log/mongodb/
mongod --fork --logpath /var/log/mongodb/mongod.log

exit_code=$?
if [ $exit_code -ne 0 ]; then
    echo "MongoDB failed to set up."
    exit $exit_code
fi

# Function to create a user if it does not already exist
create_user_if_not_exists() {
    local database_name="$1"
    local username="$2"
    local password="$3"
    local role="$4"

    if ! mongosh "$database_name" --eval "db.getUser('$username')" | grep -q "UserNotFound"; then
        echo "User '$username' already exists in database '$database_name'. Skipping creation."
    else
        mongosh "$database_name" --eval "db.createUser({ user: '$username', pwd: '$password', roles: ['$role'] })"
        echo "User '$username' created in database '$database_name'."
    fi
}

# Create the admin user if it does not already exist
create_user_if_not_exists "admin" $MONGO_ADMIN $MONGO_ADMIN_PWD "'root'"

# Create the web_scraper database
mongosh $MONGO_DB --eval "db.createCollection('data')"

# Create a regular user for the web_scraper database if it does not already exist
create_user_if_not_exists $MONGO_DB $MONGO_USER $MONGO_USER_PWD "'readWrite'"

# Output a message
echo "MongoDB setup complete."

# Stop MongoDB
mongod --shutdown

# Start MongoDB in the foreground
mongod --bind_ip 0.0.0.0
