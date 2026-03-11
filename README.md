# AI Agent Workflow Engine

Simple AI agent system that executes tasks using tool selection logic.

## Features
Task planner  
Tool execution  
FastAPI interface  
Modular tool architecture

## Tech Stack
Python  
FastAPI  
Requests

## Project Structure
agent – planning and execution logic  
tools – external tools like calculator  
api – API server

## Install

pip install -r requirements.txt

## Run

uvicorn api.server:app --reload

## Endpoint

GET /task?task=calculate 5+5
