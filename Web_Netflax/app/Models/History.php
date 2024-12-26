<?php
namespace app\Model;
use Illuminate\Database\Eloquent\Model;

class History extends Model
{
    protected $table = 'history';
    public $timestamps = false;

    protected $fillable = [
        'movie_id',
        'user_id',
    ];

    public function movie()
    {
        return $this->belongsTo(Movie::class, 'movie_id');
    }

    public function user()
    {
        return $this->belongsTo(User::class, 'user_id');
    }
}