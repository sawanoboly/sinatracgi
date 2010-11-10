#!/opt/ruby1.8.7/bin/ruby-1.8.7
require 'rubygems'
require 'sinatra'
require 'rack'


get '/' do
  'Hello World!'
end

get '/hi' do
  'Hello World 2!'
end

set :run => false, :environment => :production
Rack::Handler::CGI.run Sinatra::Application
