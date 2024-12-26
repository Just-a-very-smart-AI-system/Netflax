<?php

namespace App\Models;
use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    protected $table = 'user';
    public $timestamps = false;

    protected $fillable = [
        'user_name',
        'password',
        'email',
    ];

    public function favorites()
    {
        return $this->hasMany(Favorite::class, 'user_id');
    }

    public function histories()
    {
        return $this->hasMany(History::class, 'user_id');
    }
}
