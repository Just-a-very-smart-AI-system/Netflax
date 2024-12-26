<?php

use Illuminate\Support\Facades\Route;
use App\Models\Movies; 

Route::get('/movies', function () {
    $movies = Movies::all(); 
    return response()->json($movies);
});

Route::get('/', function () {
    return view('welcome');
});
