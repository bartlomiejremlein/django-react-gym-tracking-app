import { useEffect, useState } from "react"

function App() {
  const [inputFields, setInputFields] = useState([
    { id: "", reps: "", weight: "" },
  ])

  const [exercises, setExercises] = useState([{ id: "", name: "" }])
  const [name, setName] = useState("")
  const [date, setDate] = useState("2023-11-29")

  const getExercises = async () => {
    const response = await fetch("/api/exercises/")
    const data = await response.json()
    setExercises(data)
  }

  useEffect(() => {
    getExercises()
  }, [])

  const handleFormChange = (index, event) => {
    let data = [...inputFields]
    data[index][event.target.name] = parseInt(event.target.value)
    setInputFields(data)
  }
  const addFields = (e) => {
    e.preventDefault()
    let newField = { id: "", reps: "", weight: "" }
    setInputFields([...inputFields, newField])
  }

  const removeField = (index) => {
    let data = [...inputFields]
    data.splice(index, 1)
    setInputFields(data)
  }

  const submitForm = async (e) => {
    e.preventDefault()
    // const data = { title: "workout", exercises: inputFields }
    // console.log(inputFields)
    const formData = new FormData()
    formData.append("name", name)
    formData.append("date", date)
    formData.append("exercises", JSON.stringify(inputFields))
    console.log(formData)
    let response = await fetch("/api/exercises/add/", {
      method: "POST",
      body: formData,
    })
    const resp = await response.json()

    setInputFields([{ id: "", reps: "", weight: "" }])
    setName("")
    setDate("2023-11-29")
    // console.log(resp)
  }

  return (
    <div className='App'>
      <form onSubmit={submitForm}>
        <input
          name='name'
          placeholder='Name'
          value={name}
          onChange={(event) => setName(event.target.value)}
        />
        <input
          name='date'
          type='date'
          value={date}
          onChange={(event) => setDate(event.target.value)}
        />
        {inputFields.map((input, index) => {
          return (
            <div key={index}>
              <select
                name='id'
                type='numeric'
                onChange={(event) => handleFormChange(index, event)}
                defaultValue='0'
              >
                <option value='0' disabled>
                  None
                </option>
                {exercises.map((exercise, index) => {
                  return (
                    <option key={index} value={exercise.id}>
                      {exercise.name}
                    </option>
                  )
                })}
              </select>
              <input
                name='reps'
                placeholder='Reps'
                value={input.reps}
                onChange={(event) => handleFormChange(index, event)}
              />
              <input
                name='weight'
                placeholder='Weight'
                value={input.weight}
                onChange={(event) => handleFormChange(index, event)}
              />
              {index !== 0 ? (
                <button onClick={() => removeField(index)}>Remove</button>
              ) : (
                ""
              )}
            </div>
          )
        })}
        <button onClick={addFields}>Add More..</button>
        <button onClick={submitForm}>Submit</button>
      </form>
    </div>
  )
}

export default App
