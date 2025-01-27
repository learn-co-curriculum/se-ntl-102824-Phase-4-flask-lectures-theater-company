import { createContext, useState }   from 'react'

// 1. create the context object
const UserContext = createContext({
    user: null,
    setUser: () => {}
})

// 2. create the context provider (quasi-component)

function UserProvider({ children }){

    const [user, setUser] = useState(null)

    return (
        <UserContext.Provider value={{user, setUser}}>
            {children}
        </UserContext.Provider>
    )
}

// 3. finally, export the context and the provider

export { UserProvider, UserContext }

