import React, { useReducer, useState } from 'react';
import axios from 'axios';
import Rate from '../../components/RatingBar/Rating';




const BreedBoxPage = () => {
    const [dogs, setDogs] = useState([]);
    const [comments, setComments] = useState([]);



    const getDogList = async()=>{
        try{
            let response = await axios.get("https://dog.ceo/api/breeds/list/all")
            setDogs(response.data.items)
        }catch(error){
            console.log(error.response.data)
        };
    }

    const getComments = async()=>{
        try{
            let response = await axios.get("http://127.0.0.1:8000/api/comments/")
            setComments(response.data.items)
        }catch(error){
            console.log(error.response.data)
        };
    }


    return (
        <div>
            <button onClick={()=> {getDogList()}}>Dogs</button>
            <button onClick={()=> {getComments()}}>User Comments</button>
            <Rate />
        </div>
    )
}

export default BreedBoxPage;