local key=KEYS[1]
local current_time=tonumber(ARGV[1])
local window_size=tonumber(ARGV[2])
local limit=tonumber(ARGV[3])

redis.call("ZREMRANGEBYSCORE",key,0,current_time-window_size)

local s_size=redis.call("ZCARD",key)

if s_size>=limit then
    return {0, s_size}
end

redis.call("ZADD",key,current_time,current_time)

redis.call("EXPIRE",key,window_size)

return {1, limit-s_size-1}
