import { createContext, useState }   from 'react'

// 1. create the context object
const UserContext = createContext({
    user: null,
    setUser: () => {}
})

// 2. create the context provider (quasi-component)

function UserProvider({ children }){

    const [user, setUser] = useState(null)

    const fetchUser = () => (
        fetch('/authorized')
        .then(res => {
          if(res.ok){
            res.json()
            .then(data => {
              setUser(data)
            })
          } else {
            setUser(null)
          }
        })
      )

    return (
        <UserContext.Provider value={{user, setUser, fetchUser}}>
            {children}
        </UserContext.Provider>
    )
}

// 3. finally, export the context and the provider

export { UserProvider, UserContext }

