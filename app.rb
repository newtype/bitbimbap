require 'sinatra'
require 'sinatra/reloader' if development?

get '/' do
  rand(2) == 1 ? "Heads!" : "Tails!"
end

get /.*/ do
  redirect '/'
end
