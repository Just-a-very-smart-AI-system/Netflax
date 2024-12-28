<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\MovieController;


// Route::get('/movies', function () {
//     $movies = Movies::all(); 
//     return response()->json($movies);
// });

Route::get('/', function () {
    return view('welcome');
});

// Route::group(['prefix' => 'movie'], function(){
//     Route::get("/all", [MovieController::class, 'index'])->name('movies.index');
//     Route::get("/findId/{id}", [MovieController::class, 'show'])->name('movies.show');

//     Route::post("/create", [MovieController::class, 'store'])->name('movies.store');
// });