<?php
namespace app\Models;

use Illuminate\Database\Eloquent\Model;

class Movie extends Model
{
    protected $table = 'movies';
    public $timestamps = false;

    protected $fillable = [
        'name',
        'url',
    ];

    public function categories()
    {
        return $this->belongsToMany(Category::class, 'movie_category', 'movie_id', 'category_id');
    }

    public function favorites()
    {
        return $this->hasMany(Favorite::class, 'movie_id');
    }

    public function histories()
    {
        return $this->hasMany(History::class, 'movie_id');
    }
}